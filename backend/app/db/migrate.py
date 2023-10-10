from models.coupons import Base 
from session import engine 

if __name__ == "__main__":
    Base.metadata.create_all(engine)