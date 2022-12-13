// Copyright (c) 2021 Clumio All Rights Reserved

// Package roles contains methods related to Roles
package roles

import (
    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RolesV1 represents a custom type struct
type RolesV1 struct {
    config config.Config
}

// ListRoles Returns a list of roles that can be assigned to users, either while inviting users using the
//  [POST /users](#operation/create-user) API, or by updating the user using the
//  [PATCH /users/{user_id}](#operation/update-user) API.
func (r *RolesV1) ListRoles()(
    *models.ListRolesResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/roles"

    
    header := "application/api.clumio.roles=v1+json"
    var result *models.ListRolesResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadRole Returns a representation of the specified role.
func (r *RolesV1) ReadRole(
    roleId string)(
    *models.ReadRoleResponse, *apiutils.APIError) {

    pathURL := "/roles/{role_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "role_id": roleId,
    }
    queryBuilder := r.config.BaseUrl + pathURL

    
    header := "application/api.clumio.roles=v1+json"
    var result *models.ReadRoleResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}
