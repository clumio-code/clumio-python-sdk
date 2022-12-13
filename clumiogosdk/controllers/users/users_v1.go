// Copyright (c) 2021 Clumio All Rights Reserved

// Package users contains methods related to Users
package users

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// UsersV1 represents a custom type struct
type UsersV1 struct {
    config config.Config
}

// ListUsers Returns a list of Clumio users.
func (u *UsersV1) ListUsers(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListUsersResponse, *apiutils.APIError) {

    queryBuilder := u.config.BaseUrl + "/users"

    
    header := "application/api.clumio.users=v1+json"
    var result *models.ListUsersResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    if filter == nil {
        filter = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "filter": *filter,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: u.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreateUser Creates a new user. Specify the user's full name and email address to generate an email message that is sent to the user with an invitation to activate their Clumio account.
func (u *UsersV1) CreateUser(
    body *models.CreateUserV1Request)(
    *models.CreateUserResponse, *apiutils.APIError) {

    queryBuilder := u.config.BaseUrl + "/users"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.users=v1+json"
    var result *models.CreateUserResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: u.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// UpdateUserProfile Manages the current user's profile, such as changing the user's full name.
func (u *UsersV1) UpdateUserProfile(
    body *models.UpdateUserProfileV1Request)(
    *models.EditProfileResponse, *apiutils.APIError) {

    queryBuilder := u.config.BaseUrl + "/users/my-profile"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.users=v1+json"
    var result *models.EditProfileResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: u.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}


// ReadUser Returns a representation of the specified Clumio user.
func (u *UsersV1) ReadUser(
    userId int64)(
    *models.ReadUserResponse, *apiutils.APIError) {

    pathURL := "/users/{user_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "user_id": fmt.Sprintf("%v", userId),
    }
    queryBuilder := u.config.BaseUrl + pathURL

    
    header := "application/api.clumio.users=v1+json"
    var result *models.ReadUserResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: u.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// DeleteUser Deletes an existing user from Clumio, revoking the user's access to Clumio. A deleted user cannot be recovered.
func (u *UsersV1) DeleteUser(
    userId int64)(
    interface{}, *apiutils.APIError) {

    pathURL := "/users/{user_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "user_id": fmt.Sprintf("%v", userId),
    }
    queryBuilder := u.config.BaseUrl + pathURL

    
    header := "application/api.clumio.users=v1+json"
    var result interface{}

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: u.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}


// UpdateUser Manages an existing user. Managing a user includes enabling or disabling the user,
//  changing the user's full name or updating the user's role.
func (u *UsersV1) UpdateUser(
    userId int64, 
    body *models.UpdateUserV1Request)(
    *models.UpdateUserResponse, *apiutils.APIError) {

    pathURL := "/users/{user_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "user_id": fmt.Sprintf("%v", userId),
    }
    queryBuilder := u.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.users=v1+json"
    var result *models.UpdateUserResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: u.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}


// ChangePassword Change the password of the specified user. Users can change their own passwords.
func (u *UsersV1) ChangePassword(
    userId int64, 
    body *models.ChangePasswordV1Request)(
    interface{}, *apiutils.APIError) {

    pathURL := "/users/{user_id}/password"
    //process optional template parameters
    pathParams := map[string]string{
        "user_id": fmt.Sprintf("%v", userId),
    }
    queryBuilder := u.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.users=v1+json"
    var result interface{}

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: u.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Put,
    })

    return result, apiErr
}
