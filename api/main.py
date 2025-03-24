from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .dependencies.database import engine, get_db
from .controllers import sandwiches, orders, resources, recipes, order_details

# Create all database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# CORS settings (allow all origins for testing)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= Sandwich Endpoints =================
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db, sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich

@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    return sandwiches.update(db, sandwich_id, sandwich)

@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
def delete_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    return sandwiches.delete(db, sandwich_id)


# ================= Order Endpoints =================
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db, order)

@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)

@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    return orders.update(db, order_id, order)

@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return orders.delete(db, order_id)


# ================= Resource Endpoints =================
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db, resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    return resources.update(db, resource_id, resource)

@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_resource(resource_id: int, db: Session = Depends(get_db)):
    return resources.delete(db, resource_id)


# ================= Recipe Endpoints =================
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db, recipe)

@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    return recipes.update(db, recipe_id, recipe)

@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipes.delete(db, recipe_id)


# ================= Order Detail Endpoints =================
@app.post("/order-details/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create_order_detail(detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db, detail)

@app.get("/order-details/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)

@app.get("/order-details/{detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def read_order_detail(detail_id: int, db: Session = Depends(get_db)):
    detail = order_details.read_one(db, detail_id)
    if detail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return detail

@app.put("/order-details/{detail_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def update_order_detail(detail_id: int, detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    return order_details.update(db, detail_id, detail)

@app.delete("/order-details/{detail_id}", tags=["OrderDetails"])
def delete_order_detail(detail_id: int, db: Session = Depends(get_db)):
    return order_details.delete(db, detail_id)
