# from fastapi import FastAPI, status, HTTPException, Depends
# from fastapi.security import OAuth2PasswordRequestForm
# from fastapi.responses import RedirectResponse
# from schema import UserOut, UserAuth, TokenSchema
# from main import db
# from auth import (
#     get_hashed_password,
#     create_access_token,
#     create_refresh_token,
#     verify_password
# )

# app = FastAPI()

# @app.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = db.get(form_data.username, None)
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect email or password"
#         )

#     hashed_pass = user['password']
#     if not verify_password(form_data.password, hashed_pass):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Incorrect email or password"
#         )
    
#     return {
#         "access_token": create_access_token(user['email']),
#         "refresh_token": create_refresh_token(user['email']),
#     }