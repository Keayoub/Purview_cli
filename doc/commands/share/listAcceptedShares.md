# pvw share listAcceptedShares
[Command Reference](../../../README.md#command-reference) > [share](./main.md) > listAcceptedShares

## Description
List all data shares.

## Syntax
```
pvw share listAcceptedShares --sentShareName=<val> [--skipToken=<val>]
```

## Required Arguments
- `--sentShareName`: sentShareName parameter
- `--skipToken`: skipToken parameter

## Optional Arguments
- `--skipToken`: skipToken parameter (optional)
- `--purviewName`: The name of the Microsoft Purview account. (string)
- `--receivedShareName`: The name of the received share. (string)
- `--acceptedSentShareName`: The name of the accepted sent share. (string)
- `--assetMappingName`: The name of the asset mapping. (string)
- `--assetName`: The name of the asset. (string)
- `--invitationName`: The name of the invitation. (string)
- `--filter`: Filters the results using OData syntax. (string)
- `--orderBy`: Sorts the results using OData syntax. (string)
- `--payloadFile`: File path to a valid JSON document. (string)

## API Mapping
Share Data Plane > Share > [Listacceptedshares]()
```
 https://{accountName}.purview.azure.com/share/api/listAcceptedShares
```

## Examples
DESCRIBE_EXAMPLE.
```powershell
EXAMPLE_COMMAND
```
<details><summary>Example payload.</summary>
<p>

```json
PASTE_JSON_HERE
```
</p>
</details>