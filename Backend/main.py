from fastapi import FastAPI
from database import Base, engine
from routers import dentistasRoute, recepcionistasRoute, authRoute , adminRoute

Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(dentistasRoute.router)
app.include_router(adminRoute.router)
app.include_router(recepcionistasRoute.router)
app.include_router(authRoute.router)