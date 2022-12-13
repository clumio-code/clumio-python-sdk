// Copyright (c) 2021 Clumio All Rights Reserved

// Package apiutils has the types required for Error handling
package apiutils

// APIError structure for custom error handling in API invocation
type APIError struct {
	ResponseCode int    //The HTTP response code from the API request
	Reason       string //The reason for throwing exception
	Response     []byte
}

// NewAPIError implements initialization constructor
// Returns new APIException object
func NewAPIError(reason string, code int, res []byte) *APIError {
	ex := new(APIError)
	ex.ResponseCode = code
	ex.Reason = reason
	ex.Response = res
	return ex
}

// Error method implements error interface
func (e *APIError) Error() string {
	return e.Reason
}
