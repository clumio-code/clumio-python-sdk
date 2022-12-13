// Copyright (c) 2021 Clumio All Rights Reserved

// Package organizationalunits contains methods related to OrganizationalUnits
package organizationalunits

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// OrganizationalUnitsV1 represents a custom type struct
type OrganizationalUnitsV1 struct {
    config config.Config
}

// ListOrganizationalUnits Returns a list of organizational units.
func (o *OrganizationalUnitsV1) ListOrganizationalUnits(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListOrganizationalUnitsResponse, *apiutils.APIError) {

    queryBuilder := o.config.BaseUrl + "/organizational-units"

    
    header := "application/api.clumio.organizational-units=v1+json"
    var result *models.ListOrganizationalUnitsResponse
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
        Config: o.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreateOrganizationalUnit Create a new organizational unit.
func (o *OrganizationalUnitsV1) CreateOrganizationalUnit(
    embed *string, 
    body *models.CreateOrganizationalUnitV1Request)(
    *models.CreateOrganizationalUnitResponse, *apiutils.APIError) {

    queryBuilder := o.config.BaseUrl + "/organizational-units"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.organizational-units=v1+json"
    var result *models.CreateOrganizationalUnitResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: o.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ReadOrganizationalUnit Returns a representation of the specified organizational unit.
func (o *OrganizationalUnitsV1) ReadOrganizationalUnit(
    id string)(
    *models.ReadOrganizationalUnitResponse, *apiutils.APIError) {

    pathURL := "/organizational-units/{id}"
    //process optional template parameters
    pathParams := map[string]string{
        "id": id,
    }
    queryBuilder := o.config.BaseUrl + pathURL

    
    header := "application/api.clumio.organizational-units=v1+json"
    var result *models.ReadOrganizationalUnitResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: o.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// DeleteOrganizationalUnit Delete the specified organizational unit.
func (o *OrganizationalUnitsV1) DeleteOrganizationalUnit(
    id string, 
    embed *string)(
    *models.DeleteOrganizationalUnitResponse, *apiutils.APIError) {

    pathURL := "/organizational-units/{id}"
    //process optional template parameters
    pathParams := map[string]string{
        "id": id,
    }
    queryBuilder := o.config.BaseUrl + pathURL

    
    header := "application/api.clumio.organizational-units=v1+json"
    var result *models.DeleteOrganizationalUnitResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: o.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}


// PatchOrganizationalUnit Patch the specified organizational unit.
//  The complete updated attribute(s) of the organizational unit has to be provided in the request.
func (o *OrganizationalUnitsV1) PatchOrganizationalUnit(
    id string, 
    embed *string, 
    body *models.PatchOrganizationalUnitV1Request)(
    *models.PatchOrganizationalUnitResponse, *apiutils.APIError) {

    pathURL := "/organizational-units/{id}"
    //process optional template parameters
    pathParams := map[string]string{
        "id": id,
    }
    queryBuilder := o.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.organizational-units=v1+json"
    var result *models.PatchOrganizationalUnitResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: o.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}
