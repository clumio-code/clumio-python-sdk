// Copyright (c) 2021 Clumio All Rights Reserved

// Package autouserprovisioningrules contains methods related to AutoUserProvisioningRules
package autouserprovisioningrules

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AutoUserProvisioningRulesV1 represents a custom type struct
type AutoUserProvisioningRulesV1 struct {
    config config.Config
}

// ListAutoUserProvisioningRules Returns a list of auto user provisioning rules.
func (a *AutoUserProvisioningRulesV1) ListAutoUserProvisioningRules(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListAutoUserProvisioningRulesResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/settings/auto-user-provisioning/rules"

    
    header := "application/api.clumio.auto-user-provisioning-rules=v1+json"
    var result *models.ListAutoUserProvisioningRulesResponse
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
        Config: a.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreateAutoUserProvisioningRule Creates a new auto user provisioning rule. Auto user provisioning rules determine the role and
//  organizational units to be assigned to a user subject to the condition.
func (a *AutoUserProvisioningRulesV1) CreateAutoUserProvisioningRule(
    body *models.CreateAutoUserProvisioningRuleV1Request)(
    *models.CreateAutoUserProvisioningRuleResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/settings/auto-user-provisioning/rules"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.auto-user-provisioning-rules=v1+json"
    var result *models.CreateAutoUserProvisioningRuleResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ReadAutoUserProvisioningRule Returns a representation of the specified auto user provisioning rule.
func (a *AutoUserProvisioningRulesV1) ReadAutoUserProvisioningRule(
    ruleId string)(
    *models.ReadAutoUserProvisioningRuleResponse, *apiutils.APIError) {

    pathURL := "/settings/auto-user-provisioning/rules/{rule_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "rule_id": ruleId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    
    header := "application/api.clumio.auto-user-provisioning-rules=v1+json"
    var result *models.ReadAutoUserProvisioningRuleResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// UpdateAutoUserProvisioningRule Update an existing auto user provisioning rule.
func (a *AutoUserProvisioningRulesV1) UpdateAutoUserProvisioningRule(
    ruleId string, 
    body *models.UpdateAutoUserProvisioningRuleV1Request)(
    *models.UpdateAutoUserProvisioningRuleResponse, *apiutils.APIError) {

    pathURL := "/settings/auto-user-provisioning/rules/{rule_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "rule_id": ruleId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.auto-user-provisioning-rules=v1+json"
    var result *models.UpdateAutoUserProvisioningRuleResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Put,
    })

    return result, apiErr
}


// DeleteAutoUserProvisioningRule Delete the specified auto user provisioning rule.
func (a *AutoUserProvisioningRulesV1) DeleteAutoUserProvisioningRule(
    ruleId string)(
    interface{}, *apiutils.APIError) {

    pathURL := "/settings/auto-user-provisioning/rules/{rule_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "rule_id": ruleId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    
    header := "application/api.clumio.auto-user-provisioning-rules=v1+json"
    var result interface{}

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}
