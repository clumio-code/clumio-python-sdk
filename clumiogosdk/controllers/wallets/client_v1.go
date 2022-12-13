// Copyright (c) 2021 Clumio All Rights Reserved

package wallets

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// WalletsV1Client represents a custom type interface
type WalletsV1Client interface {
    // ListWallets Returns a list of wallets.
    ListWallets(
        limit *int64, 
        start *string)(
        *models.ListWalletsResponse,  *apiutils.APIError)
    
    // CreateWallet Create a wallet.
    CreateWallet(
        body *models.CreateWalletV1Request)(
        *models.CreateWalletResponse,  *apiutils.APIError)
    
    // ReadWallet Returns a representation of the specified KMS wallet.
    ReadWallet(
        walletId string)(
        *models.ReadWalletResponse,  *apiutils.APIError)
    
    // DeleteWallet Delete the wallet with the specified id.
    DeleteWallet(
        walletId string)(
        interface{},  *apiutils.APIError)
    
    // RefreshWallet Refresh the access status of a wallet with the specified id to verify if it can be used for backup/restore.
    RefreshWallet(
        walletId string)(
        *models.RefreshWalletResponse,  *apiutils.APIError)
    
}

// NewWalletsV1 returns WalletsV1Client
func NewWalletsV1(config config.Config) WalletsV1Client {
    client := new(WalletsV1)
    client.config = config
    return client
}
