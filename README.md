

# Image Uploader REST API build in Django

This project is a Django REST Framework API that allows users to upload PNG or JPG images and view them later. Users can upload images via HTTP requests and view their uploaded images through the API. The API has three built-in account tiers: 

Basic, Premium, and Enterprise


 - Users with the Basic plan receive a link to a 200px thumbnail after
   uploading an image.


 - Premium users receive a link to a 200px thumbnail, a 400px thumbnail,
   and a link to the originally uploaded image.


 - Enterprise users receive a link to a 200px thumbnail, a 400px
   thumbnail, a link to the originally uploaded image, and the ability
   to generate expiring links to the binary image.

Admins can create custom account tiers with configurable thumbnail sizes, the presence of the link to the originally uploaded file, and the ability to generate expiring links. The admin UI is accessible through Django's admin panel, and there is no custom user UI.

To run the project, simply clone the repository and run it with Docker Compose. Then use commands:

  ```
  docker ps
  ```
  ```
  docker exec -it <name> bash
  ```
  ```
  python manage.py makemigrations
  ```
  ```
  python manage.py migrate
  ```
  ```
  python manage.py createsuperuser
  ```

 




## API Reference

#### Upload photo

```http
  POST /api/file-upload/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Title` | `string` | **not required**|
| `Description` | `string` | **not required**|
| `image_url` | `file` | **required**|

#### User photo list

```http
  GET /api/file-list/
```
#### Photo details
```http
  GET /api/file-details/<int:pk>
```
#### Delete photo
```http
  DELETE /api/file-delete/<int:pk>
```
#### Generate links
```http
  GET /api/generate-links/
```



#### Generate links list
```http
  GET /api/generate-links/
```
#### Generated link details
```http
  GET /api/generate-link-details/<int:pk>
```

