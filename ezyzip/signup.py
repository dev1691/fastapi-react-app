# from fastapi import FastAPI
# from fastapi import status
# from fastapi import HTTPException
# from fastapi.responses import RedirectResponse
# from schema import UserOut, UserAuth
# from main import db
# from auth import get_hashed_password

# app = FastAPI()

# @app.post('/signup', summary="Create new user", response_model=UserOut)
# async def create_user(data: UserAuth):f
#     # querying database to check if user already exist
#     user = db.get(data.email, None)
#     if user is not None:
#             raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User with this email already exist"
#         )
#     user = {
#         'email': data.email,
#         'password_': get_hashed_password(data.password_),

#     }
#     db[data.email] = user    # saving user to database
#     return user