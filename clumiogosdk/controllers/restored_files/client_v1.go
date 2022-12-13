// Copyright (c) 2021 Clumio All Rights Reserved

package restoredfiles

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredFilesV1Client represents a custom type interface
type RestoredFilesV1Client interface {
    // ListRestoredFiles Gets the list of active restored files for an asset.
    ListRestoredFiles(
        limit *int64, 
        start *string, 
        filter string)(
        *models.RestoredFilesResponse,  *apiutils.APIError)
    
    // RestoreFiles Restores one or more files from the specified backup.
    RestoreFiles(
        embed *string, 
        body models.RestoreFilesV1Request)(
        *models.RestoreFileResponse,  *apiutils.APIError)
    
    // DownloadSharedFile Downloads one or more restored files, bundled into a ZIP file, that another user shared with you by email.
    DownloadSharedFile(
        body *models.DownloadSharedFileV1Request)(
        *models.DownloadSharedFileResponse,  *apiutils.APIError)
    
    // GenerateRestoredFilePasscode Generates a new passcode to access restored files shared by email. A passcode is
    //  automatically generated when you share restored files by email. Only regenerate a
    //  passcode if you (or the recipient) have lost the original passcode. When you
    //  regenerate a new passcode, the old one becomes invalid.
    GenerateRestoredFilePasscode(
        restoredFileId string)(
        *models.GenerateRestoredFilePasscodeResponse,  *apiutils.APIError)
    
    // ShareRestoredFile Sends a downloadable link to the specified email recipient to access restored files
    //  shared by email. Restored files are initially sent by email using
    //  [POST /restores/files](#operation/restore-files). After you send the initial email to one user, you can run
    //  this endpoint to share the email with additional users or to resend the email to
    //  the initial user. Also send the passcode generated from
    //  [POST /restores/files](#operation/restore-files) to these users so they can access
    //  the restored files.
    ShareRestoredFile(
        restoredFileId string, 
        body *models.ShareRestoredFileV1Request)(
        *models.ShareFileRestoreEmailResponse,  *apiutils.APIError)
    
}

// NewRestoredFilesV1 returns RestoredFilesV1Client
func NewRestoredFilesV1(config config.Config) RestoredFilesV1Client {
    client := new(RestoredFilesV1)
    client.config = config
    return client
}
