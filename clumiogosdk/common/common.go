// Copyright (c) 2022 Clumio All Rights Reserved

package common

import (
	"fmt"

	apiutils "github.com/clumio-code/clumio-go-sdk/api_utils"
	"github.com/clumio-code/clumio-go-sdk/config"
	"github.com/go-resty/resty/v2"
)

const (
	sdkVersion = "SDK_VERSION"

	AcceptHeader         = "Accept"
	OrgUnitContextHeader = "x-clumio-organizationalunit-context"
	ApiClientHeader      = "x-clumio-api-client"
	SDKVersionHeader     = "x-clumio-sdk-version"

	InternalServerError       = "Internal Server Error"
	NonSuccessStatusCodeError = "Non-success status code returned."

	Get    = "GET"
	Post   = "POST"
	Put    = "PUT"
	Patch  = "PATCH"
	Delete = "DELETE"
)

// InvokeAPIRequest contains the parameters required for InvokeAPI.
type InvokeAPIRequest struct {
	AcceptHeader  string
	Body          string
	Config        config.Config
	PathParams    map[string]string
	QueryParams   map[string]string
	RequestType   string
	RequestUrl    string
	Result        interface{}
}

// InvokeAPI invokes the REST API and returns an error if it fails.
func InvokeAPI(request *InvokeAPIRequest) *apiutils.APIError {
	client := resty.New()
	req := client.R().
		SetHeader(AcceptHeader, request.AcceptHeader).
		SetHeader(OrgUnitContextHeader, request.Config.OrganizationalUnitContext).
		SetHeader(ApiClientHeader, "clumio-go-sdk").
		SetHeader(SDKVersionHeader, fmt.Sprintf("clumio-go-sdk:%v", sdkVersion)).
		SetAuthToken(request.Config.Token).
		SetResult(request.Result)

	if request.Config.CustomHeaders != nil {
		for headerKey, headerValue := range request.Config.CustomHeaders {
			req.SetHeader(headerKey, headerValue)
		}
	}

	if request.QueryParams != nil {
		req.SetQueryParams(request.QueryParams)
	}

	if request.PathParams != nil {
		req.SetPathParams(request.PathParams)
	}

	if request.Body != "" {
		req.SetBody(request.Body)
	}

	var response *resty.Response
	var err error
	switch request.RequestType {
	case Get:
		response, err = req.Get(request.RequestUrl)
	case Post:
		response, err = req.Post(request.RequestUrl)
	case Put:
		response, err = req.Put(request.RequestUrl)
	case Patch:
		response, err = req.Patch(request.RequestUrl)
	case Delete:
		response, err = req.Delete(request.RequestUrl)
	}

	if err != nil {
		return &apiutils.APIError{
			ResponseCode: 500,
			Reason:       InternalServerError,
			Response:     []byte(fmt.Sprintf("%v", err)),
		}
	}
	if !response.IsSuccess() {
		return &apiutils.APIError{
			ResponseCode: response.RawResponse.StatusCode,
			Reason:       NonSuccessStatusCodeError,
			Response:     response.Body(),
		}
	}
	return nil
}
