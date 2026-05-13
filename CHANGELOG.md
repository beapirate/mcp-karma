# Changelog

## [0.10.2](https://github.com/intenthq/mcp-karma/compare/v0.10.1...v0.10.2) (2026-05-13)


### Bug Fixes

* reuse a single httpx.AsyncClient for tool calls ([#31](https://github.com/intenthq/mcp-karma/issues/31)) ([1501835](https://github.com/intenthq/mcp-karma/commit/1501835d66130e6dbc41b4bec53ef0e8bf9ad552))
* use GitHub App token for release-please so deploys trigger ([#30](https://github.com/intenthq/mcp-karma/issues/30)) ([ff5c9ef](https://github.com/intenthq/mcp-karma/commit/ff5c9ef9305f7c31cfd571bbca2404fc25c5a93f))

## [0.10.1](https://github.com/intenthq/mcp-karma/compare/v0.10.0...v0.10.1) (2026-05-05)


### Miscellaneous Chores

* **deps:** update python docker tag to v3.14 ([#26](https://github.com/intenthq/mcp-karma/issues/26)) ([b39ccd6](https://github.com/intenthq/mcp-karma/commit/b39ccd61e07256ffa20bd59c2f594bc62fca63d4))
* drop component prefix from release-please tags ([#23](https://github.com/intenthq/mcp-karma/issues/23)) ([57ef5ee](https://github.com/intenthq/mcp-karma/commit/57ef5ee0148257e7f407754c05f8f5d657e17b70))
* pin actions to SHAs and surface chore/deps in releases ([#27](https://github.com/intenthq/mcp-karma/issues/27)) ([5bf40b2](https://github.com/intenthq/mcp-karma/commit/5bf40b2bcfbf5992241e8a4cfcc6812854ff261b))
* Update astral-sh/setup-uv action to v8 ([#24](https://github.com/intenthq/mcp-karma/issues/24)) ([832b70d](https://github.com/intenthq/mcp-karma/commit/832b70dfef815b8f1d10809b657a48a522b0e00b))
* Update googleapis/release-please-action action to v5 ([#25](https://github.com/intenthq/mcp-karma/issues/25)) ([ed837e2](https://github.com/intenthq/mcp-karma/commit/ed837e2bd2da47c66d1940beec477f6745219a6e))
* Update tj-actions/changed-files action to v47.0.6 ([#28](https://github.com/intenthq/mcp-karma/issues/28)) ([749c16b](https://github.com/intenthq/mcp-karma/commit/749c16bcf21de45fe096d621c364293fb5261786))

## [0.10.0](https://github.com/intenthq/mcp-karma/compare/karma-mcp-v0.9.3...karma-mcp-v0.10.0) (2026-04-29)


### Features

* add list_alerts_by_label tool with optional cluster scope ([#17](https://github.com/intenthq/mcp-karma/issues/17)) ([43e42c6](https://github.com/intenthq/mcp-karma/commit/43e42c6dac2790ed3952b9c7a60a53a2d9d8b69b))


### Bug Fixes

* apply ruff formatting to server.py ([2b0db00](https://github.com/intenthq/mcp-karma/commit/2b0db00233b532acf356c7538251ab22d3560082))
* apply ruff formatting to server.py ([ee7d554](https://github.com/intenthq/mcp-karma/commit/ee7d554b64af00ea9533ca86408f7a853b61f4f1))
* extract severity from Karma shared labels ([69c4d92](https://github.com/intenthq/mcp-karma/commit/69c4d92a88f6664f12232e0de1b134a65745e0f6))
* extract severity from Karma shared labels ([67bb4a1](https://github.com/intenthq/mcp-karma/commit/67bb4a17e696dc7e310c0ef5bae52bee13164e75))
* resolve severity label from both group and alert labels ([d8d496d](https://github.com/intenthq/mcp-karma/commit/d8d496d7fedb56b9c9699b4214084db780dcc66a))
* resolve severity label from both group and alert labels ([f3fe994](https://github.com/intenthq/mcp-karma/commit/f3fe99403dde16e542bc6568f64c71dec0b570ab))
* restore HTTP server as Docker entrypoint ([4ce6c46](https://github.com/intenthq/mcp-karma/commit/4ce6c46393b40b43a43f4fb4a680be7457356176))
* restore HTTP server as Docker entrypoint ([9b9fce2](https://github.com/intenthq/mcp-karma/commit/9b9fce2add25cdb4a0ada96d22b109388f58122e))
* switch Docker image registry from DockerHub to GHCR ([4840e6a](https://github.com/intenthq/mcp-karma/commit/4840e6a11816e04f2ddc140ded23306dee7dfdaf))
