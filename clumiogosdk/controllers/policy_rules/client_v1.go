// Copyright (c) 2021 Clumio All Rights Reserved

package policyrules

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// PolicyRulesV1Client represents a custom type interface
type PolicyRulesV1Client interface {
    // ListPolicyRules Returns a list of policy rules.
    ListPolicyRules(
        limit *int64, 
        start *string, 
        organizationalUnitId *string, 
        sort *string, 
        filter *string)(
        *models.ListRulesResponse,  *apiutils.APIError)
    
    // CreatePolicyRule Creates a new policy rule. Policy rules determine how a policy should be assigned to assets.
    //  Additionally, to create a rule in the context of another Organizational Unit, refer to the
    //  Getting Started documentation.
    CreatePolicyRule(
        body *models.CreatePolicyRuleV1Request)(
        *models.CreateRuleResponse,  *apiutils.APIError)
    
    // ReadPolicyRule Returns a representation of the specified policy rule.
    ReadPolicyRule(
        ruleId string)(
        *models.ReadRuleResponse,  *apiutils.APIError)
    
    // UpdatePolicyRule Updates an existing policy rule.
    UpdatePolicyRule(
        ruleId string, 
        body *models.UpdatePolicyRuleV1Request)(
        *models.UpdateRuleResponse,  *apiutils.APIError)
    
    // DeletePolicyRule Deletes the specified policy rule.
    DeletePolicyRule(
        ruleId string)(
        *models.DeleteRuleResponse,  *apiutils.APIError)
    
}

// NewPolicyRulesV1 returns PolicyRulesV1Client
func NewPolicyRulesV1(config config.Config) PolicyRulesV1Client {
    client := new(PolicyRulesV1)
    client.config = config
    return client
}
