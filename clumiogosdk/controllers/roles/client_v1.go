// Copyright (c) 2021 Clumio All Rights Reserved

package roles

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RolesV1Client represents a custom type interface
type RolesV1Client interface {
    // ListRoles Returns a list of roles that can be assigned to users, either while inviting users using the
    //  [POST /users](#operation/create-user) API, or by updating the user using the
    //  [PATCH /users/{user_id}](#operation/update-user) API.
    ListRoles()(
        *models.ListRolesResponse,  *apiutils.APIError)
    
    // ReadRole Returns a representation of the specified role.
    ReadRole(
        roleId string)(
        *models.ReadRoleResponse,  *apiutils.APIError)
    
}

// NewRolesV1 returns RolesV1Client
func NewRolesV1(config config.Config) RolesV1Client {
    client := new(RolesV1)
    client.config = config
    return client
}
