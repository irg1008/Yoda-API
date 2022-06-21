# YODA API

An api for
[yoda-fits (first intergalactic title shortener)](https://github.com/irg1008/Yoda)
made with deno and openapi specifications.

## Deno tools

- Linter = `deno lint`

- Formatter = `deno fmt`

- Testing = `deno test`

See full list of tools [here](https://deno.land/manual/tools).

## Deno runtime permission flags

- `--allow-net`
- `--allow-read`

See full list of flags
[here](https://deno.land/manual/getting_started/permissions).

## Cheatsheet from deno to node

[Deno2Node Cheatsheet](https://deno.land/manual/node/cheatsheet)

## Packages used

- [denodb](https://deno.land/x/denodb@v1.0.40)
- [opine](https://deno.land/x/opine@2.2.0)

## How to run this app

`deno run --import-map=import_map.json --allow-env --allow-read --allow-net .\app.ts`

### Using velociraptor

`vr start`
