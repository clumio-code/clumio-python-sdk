// Copyright (c) 2021 Clumio All Rights Reserved

// Package config has the types required for configuration
package config

type Config struct {
	Token                     string
	BaseUrl                   string
	OrganizationalUnitContext string
	CustomHeaders             map[string]string
}
