// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredfiles contains methods related to RestoredFiles
package restoredfiles

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredFilesV1 represents a custom type struct
type RestoredFilesV1 struct {
    config config.Config
}

// ListRestoredFiles Gets the list of active restored files for an asset.
func (r *RestoredFilesV1) ListRestoredFiles(
    limit *int64, 
    start *string, 
    filter string)(
    *models.RestoredFilesResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/files"

    
    header := "application/api.clumio.restored-files=v1+json"
    var result *models.RestoredFilesResponse
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
        "filter": filter,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// RestoreFiles Restores one or more files from the specified backup.
func (r *RestoredFilesV1) RestoreFiles(
    embed *string, 
    body models.RestoreFilesV1Request)(
    *models.RestoreFileResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/files"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-files=v1+json"
    var result *models.RestoreFileResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// DownloadSharedFile Downloads one or more restored files, bundled into a ZIP file, that another user shared with you by email.
func (r *RestoredFilesV1) DownloadSharedFile(
    body *models.DownloadSharedFileV1Request)(
    *models.DownloadSharedFileResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/files/_download"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-files=v1+json"
    var result *models.DownloadSharedFileResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// GenerateRestoredFilePasscode Generates a new passcode to access restored files shared by email. A passcode is
//  automatically generated when you share restored files by email. Only regenerate a
//  passcode if you (or the recipient) have lost the original passcode. When you
//  regenerate a new passcode, the old one becomes invalid.
func (r *RestoredFilesV1) GenerateRestoredFilePasscode(
    restoredFileId string)(
    *models.GenerateRestoredFilePasscodeResponse, *apiutils.APIError) {

    pathURL := "/restores/files/{restored_file_id}/_generate_passcode"
    //process optional template parameters
    pathParams := map[string]string{
        "restored_file_id": restoredFileId,
    }
    queryBuilder := r.config.BaseUrl + pathURL

    
    header := "application/api.clumio.restored-files=v1+json"
    var result *models.GenerateRestoredFilePasscodeResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}


// ShareRestoredFile Sends a downloadable link to the specified email recipient to access restored files
//  shared by email. Restored files are initially sent by email using
//  [POST /restores/files](#operation/restore-files). After you send the initial email to one user, you can run
//  this endpoint to share the email with additional users or to resend the email to
//  the initial user. Also send the passcode generated from
//  [POST /restores/files](#operation/restore-files) to these users so they can access
//  the restored files.
func (r *RestoredFilesV1) ShareRestoredFile(
    restoredFileId string, 
    body *models.ShareRestoredFileV1Request)(
    *models.ShareFileRestoreEmailResponse, *apiutils.APIError) {

    pathURL := "/restores/files/{restored_file_id}/_share"
    //process optional template parameters
    pathParams := map[string]string{
        "restored_file_id": restoredFileId,
    }
    queryBuilder := r.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-files=v1+json"
    var result *models.ShareFileRestoreEmailResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
