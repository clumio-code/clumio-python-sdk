// Copyright (c) 2021 Clumio All Rights Reserved

package autouserprovisioningrules

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AutoUserProvisioningRulesV1Client represents a custom type interface
type AutoUserProvisioningRulesV1Client interface {
    // ListAutoUserProvisioningRules Returns a list of auto user provisioning rules.
    ListAutoUserProvisioningRules(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListAutoUserProvisioningRulesResponse,  *apiutils.APIError)
    
    // CreateAutoUserProvisioningRule Creates a new auto user provisioning rule. Auto user provisioning rules determine the role and
    //  organizational units to be assigned to a user subject to the condition.
    CreateAutoUserProvisioningRule(
        body *models.CreateAutoUserProvisioningRuleV1Request)(
        *models.CreateAutoUserProvisioningRuleResponse,  *apiutils.APIError)
    
    // ReadAutoUserProvisioningRule Returns a representation of the specified auto user provisioning rule.
    ReadAutoUserProvisioningRule(
        ruleId string)(
        *models.ReadAutoUserProvisioningRuleResponse,  *apiutils.APIError)
    
    // UpdateAutoUserProvisioningRule Update an existing auto user provisioning rule.
    UpdateAutoUserProvisioningRule(
        ruleId string, 
        body *models.UpdateAutoUserProvisioningRuleV1Request)(
        *models.UpdateAutoUserProvisioningRuleResponse,  *apiutils.APIError)
    
    // DeleteAutoUserProvisioningRule Delete the specified auto user provisioning rule.
    DeleteAutoUserProvisioningRule(
        ruleId string)(
        interface{},  *apiutils.APIError)
    
}

// NewAutoUserProvisioningRulesV1 returns AutoUserProvisioningRulesV1Client
func NewAutoUserProvisioningRulesV1(config config.Config) AutoUserProvisioningRulesV1Client {
    client := new(AutoUserProvisioningRulesV1)
    client.config = config
    return client
}
