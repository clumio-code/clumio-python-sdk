// Copyright (c) 2021 Clumio All Rights Reserved

package users

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// UsersV1Client represents a custom type interface
type UsersV1Client interface {
    // ListUsers Returns a list of Clumio users.
    ListUsers(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListUsersResponse,  *apiutils.APIError)
    
    // CreateUser Creates a new user. Specify the user's full name and email address to generate an email message that is sent to the user with an invitation to activate their Clumio account.
    CreateUser(
        body *models.CreateUserV1Request)(
        *models.CreateUserResponse,  *apiutils.APIError)
    
    // UpdateUserProfile Manages the current user's profile, such as changing the user's full name.
    UpdateUserProfile(
        body *models.UpdateUserProfileV1Request)(
        *models.EditProfileResponse,  *apiutils.APIError)
    
    // ReadUser Returns a representation of the specified Clumio user.
    ReadUser(
        userId int64)(
        *models.ReadUserResponse,  *apiutils.APIError)
    
    // DeleteUser Deletes an existing user from Clumio, revoking the user's access to Clumio. A deleted user cannot be recovered.
    DeleteUser(
        userId int64)(
        interface{},  *apiutils.APIError)
    
    // UpdateUser Manages an existing user. Managing a user includes enabling or disabling the user,
    //  changing the user's full name or updating the user's role.
    UpdateUser(
        userId int64, 
        body *models.UpdateUserV1Request)(
        *models.UpdateUserResponse,  *apiutils.APIError)
    
    // ChangePassword Change the password of the specified user. Users can change their own passwords.
    ChangePassword(
        userId int64, 
        body *models.ChangePasswordV1Request)(
        interface{},  *apiutils.APIError)
    
}

// NewUsersV1 returns UsersV1Client
func NewUsersV1(config config.Config) UsersV1Client {
    client := new(UsersV1)
    client.config = config
    return client
}
