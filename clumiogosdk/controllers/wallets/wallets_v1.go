// Copyright (c) 2021 Clumio All Rights Reserved

// Package wallets contains methods related to Wallets
package wallets

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// WalletsV1 represents a custom type struct
type WalletsV1 struct {
    config config.Config
}

// ListWallets Returns a list of wallets.
func (w *WalletsV1) ListWallets(
    limit *int64, 
    start *string)(
    *models.ListWalletsResponse, *apiutils.APIError) {

    queryBuilder := w.config.BaseUrl + "/wallets"

    
    header := "application/api.clumio.wallets=v1+json"
    var result *models.ListWalletsResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: w.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreateWallet Create a wallet.
func (w *WalletsV1) CreateWallet(
    body *models.CreateWalletV1Request)(
    *models.CreateWalletResponse, *apiutils.APIError) {

    queryBuilder := w.config.BaseUrl + "/wallets"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.wallets=v1+json"
    var result *models.CreateWalletResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: w.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ReadWallet Returns a representation of the specified KMS wallet.
func (w *WalletsV1) ReadWallet(
    walletId string)(
    *models.ReadWalletResponse, *apiutils.APIError) {

    pathURL := "/wallets/{wallet_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "wallet_id": walletId,
    }
    queryBuilder := w.config.BaseUrl + pathURL

    
    header := "application/api.clumio.wallets=v1+json"
    var result *models.ReadWalletResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: w.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// DeleteWallet Delete the wallet with the specified id.
func (w *WalletsV1) DeleteWallet(
    walletId string)(
    interface{}, *apiutils.APIError) {

    pathURL := "/wallets/{wallet_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "wallet_id": walletId,
    }
    queryBuilder := w.config.BaseUrl + pathURL

    
    header := "application/api.clumio.wallets=v1+json"
    var result interface{}

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: w.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Delete,
    })

    return result, apiErr
}


// RefreshWallet Refresh the access status of a wallet with the specified id to verify if it can be used for backup/restore.
func (w *WalletsV1) RefreshWallet(
    walletId string)(
    *models.RefreshWalletResponse, *apiutils.APIError) {

    pathURL := "/wallets/{wallet_id}/_refresh"
    //process optional template parameters
    pathParams := map[string]string{
        "wallet_id": walletId,
    }
    queryBuilder := w.config.BaseUrl + pathURL

    
    header := "application/api.clumio.wallets=v1+json"
    var result *models.RefreshWalletResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: w.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
