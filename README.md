This Django E-commerce platform is a marketplace for connecting beauty brands and dermatologists to consumers. 
The API is developed using Django REST Framework serving as the backend for managing products on the e-commerce platform, allowing users to create, update, delete, and view products. 


A.	FUNCTIONAL REQUIREMENTS:

PRODUCT MANAGEMENT (CRUD):
Users have the ability to Create, Read, Update, and Delete (CRUD) products.
Each product has the following attributes: Name, Description, Price, Category, Stock Quantity, Image, and Created By and Created Date.
Validation is required to update fields like Price, Name, and Stock Quantity.

USERS MANAGEMENT (CRUD):
CRUD operations for users who manage the products.
A user has a unique Username, Email, and Password.
Only authenticated users can be able to manage products (i.e., create, update, delete).

PRODUCT SEARCH:
Endpoint to search for products by Name or Category.
Partial matches in product names for flexible search results.
Pagination for search results to improve performance when there are many products.

PRODUCT VIEW:
Endpoint to retrieve a list of products or view individual product details by Product ID.
Includes an optional filter for users to view products by Category, Price Range, or Stock Availability.
Product details include all relevant information like Name, Description, Price, Category, Stock Quantity, and Image.


B.	TECHNICAL REQUIREMENTS:  

DATABASE:
Django ORM to interact with the database.
Models for Products, Categories and Users.
Each product is associated with a category for better organization (e.g., skincare, haircare, aesthetics.).

AUTHENTICATION:
User authentication using Django’s built-in authentication system.
Only authenticated users are able to perform CRUD operations on products.
Token-based authentication (JWT) to secure the API.

API DESIGN:
Django Rest Framework (DRF) used to design and expose API endpoints.
RESTful principles by using appropriate HTTP methods (GET, POST, PUT, DELETE).
Proper error handling, returning appropriate HTTP status codes for various actions (e.g., 404 for not found, 400 for bad request).

DEPLOYMENT:
API accessible, stable, and secure.


C.  FUTURE GOALS 

Artificial Intelligence: Integrate machine learning for image recognition and product recommendation system.  

Dermatologists dashboard: Gain access to customer AI analysis reports and provide virtual consultations to clients.

Product Reviews: To allow users to submit reviews and ratings for products and an endpoint to retrieve product reviews.

Product Images: Allow users to upload multiple images for products, storing the image URLs in the database.

Wishlist: Add a feature where users can add products to a wishlist, with endpoints to manage this functionality.

Stock Management: Implement an automatic stock reduction system when a user “purchases” a product (or mark it as reserved).

Discounts and Promotions: Add functionality for users to create promotional discounts on certain products, applying price reductions accordingly

AI Models: To provide analysis and recommendation capabilities.
