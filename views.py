from django.shortcuts import render
from django.conf import settings
from .models import *
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os
import time

# Define the classes
all_classes = ['FreshApple', 'RottenApple', 'FreshBanana', 'RottenBanana', 'FreshMango', 'RottenMango',
               'FreshOrange', 'RottenOrange', 'FreshStrawberry', 'RottenStrawberry', 'FreshCarrot', 'RottenCarrot',
               'FreshTomato', 'RottenTomato', 'FreshCucumber', 'RottenCucumber', 'FreshPotato', 'RottenPotato',
               'FreshBellpepper', 'RottenBellpepper']

model_path = os.path.join(settings.BASE_DIR, 'freshness_detector', 'model', 'freshness_model.h5')
model = tf.keras.models.load_model(model_path)


def predict_image(image_path):
    start_time = time.time()

    img = load_img(image_path, target_size=(150, 150))
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    predicted_class_index = tf.argmax(predictions[0]).numpy()
    predicted_class = all_classes[predicted_class_index]
    confidence_score = predictions[0][predicted_class_index]

    end_time = time.time()
    time_taken = end_time - start_time

    return predicted_class, confidence_score, time_taken


def freshness_detector(request):
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        image_path = os.path.join(settings.MEDIA_ROOT, 'uploads', uploaded_image.name)

        with open(image_path, 'wb+') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

        predicted_class, confidence_score, time_taken = predict_image(image_path)

        prediction = FreshnessPrediction.objects.create(
            image='uploads/' + uploaded_image.name,
            predicted_class=predicted_class,
            confidence_score=confidence_score,
            time_taken=time_taken
        )

        context = {
            'predicted_class': predicted_class,
            'confidence_score': confidence_score,
            'time_taken': time_taken,
            'image_uploaded': True,
            'uploaded_image_url': prediction.image.url,
            'uploaded_image_name': uploaded_image.name
        }

        return render(request, 'freshness_detector.html', context)

    return render(request, 'freshness_detector.html')


def history(request):
    predictions = FreshnessPrediction.objects.all().order_by('-uploaded_at')
    return render(request, 'freshness_detector_history.html', {'predictions': predictions})
