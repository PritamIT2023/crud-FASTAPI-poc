from db.database import engine, get_db
import db.Models as Models
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.schemas import Products
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Create all tables in the database based on the defined models
Models.Base.metadata.create_all(bind=engine)

@app.post("/product", tags=["Products"], summary="Create a new product") 
def create(product: Products, db: Session = Depends(get_db)):
    """
    Create a new product.
    
    This endpoint allows you to add a new product to the database.
    """
    try:
        # Convert the Pydantic model to a dictionary and unpack it to create a SQLAlchemy model instance
        db_product = Models.Product(**product.model_dump())
        
        # Add the new product to the database session
        db.add(db_product)
        
        # Commit the transaction to save the product to the database
        db.commit()
        
        # Refresh the product instance to ensure it reflects the current database state
        db.refresh(db_product)
        
        # Return the created product, which now includes the database-generated ID
        return db_product
    except Exception as e:
        # If an error occurs during creation, rollback the transaction
        db.rollback()
        # Raise an HTTP 400 error with the error details
        raise HTTPException(status_code=400, detail=f"Failed to create product: {str(e)}")

@app.get("/products",  tags=["Products"], summary="Get all products")
def read_products(db: Session = Depends(get_db)):
    # Query the database for all products
    products = db.query(Models.Product).all()

    # Return the list of products
    return products

@app.get("/product/{product_id}",  tags=["Products"], summary="Get a product by ID")
def read_product(product_id: int, db: Session = Depends(get_db)):
    # Query the database for a product with the given ID
    product = db.query(Models.Product).filter(Models.Product.id == product_id).first()
    
    if product is None:
        # If the product is not found, raise a 404 error
        raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found")
    
    # Return the found product
    return product


@app.put("/product/{product_id}",  tags=["Products"], summary="Update a product by ID")
def update_product(product_id: int, product: Products, db: Session = Depends(get_db)):
    # Query the database for the product with the given ID
    db_product = db.query(Models.Product).filter(Models.Product.id == product_id).first()
    
    if db_product:
        # Update the product attributes with the new values
        for key, value in product.model_dump().items():
            setattr(db_product, key, value)
        
        # Commit the changes to the database
        db.commit()
        
        # Refresh the product instance to ensure it reflects the current database state
        db.refresh(db_product)
        
        return db_product
    else:
        # If the product doesn't exist, return a 404 error
        raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/product/{product_id}",  tags=["Products"], summary="Delete a product by ID")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    # Query the database for the product with the given ID
    product = db.query(Models.Product).filter(Models.Product.id == product_id).first()
    
    # If the product exists, delete it from the database
    if product:
        db.delete(product)
        db.commit()
        return {"message": "Product deleted successfully"}
    else:
        # If the product doesn't exist, return a 404 error
        raise HTTPException(status_code=404, detail="Product not found")
