# MSTeams Resource

Send Message Cards to MS Teams

## Package Source

This package is hosted with Github Container Registry and can be found:

[`ghcr.io/wtw-im/concourse-msteams-resource/msteams-resource`](ghcr.io/wtw-im/concourse-msteams-resource/msteams-resource)

## Source Configuration
* `url`: *Required.* The URL to POST the message card to.
* `log_level`: Controls the verbosity of log messages. Possible values: `debug`, `info`, `warn`, or `error`. Default is `info`.

## Parameters

There are 2 different ways to send a card.
### Simple Card

A simple Message Card interface.

* `summary`: *Required.* The summary shown in compact view.
* `title`: The card's title
* `text`: The body of the card
* `themeColor`: The card's color

#### Example

``` yaml
params:
  summary: A summary of the card.
  title: The title of the card.
  text: This is the message body of the card.
  themeColor: "35495c"
```

### Message Card Template YML

* `template`: *Required.* A YML-representation of a [Microsoft's Legacy Actionable Message Card](https://docs.microsoft.com/en-us/outlook/actionable-messages/message-card-reference).

Variables are wrapped with `{}` and are defined under `vars`.

* `vars`: *Required* if consuming variables in the template. Each variable can have the following configuration:

  * `file`: the contents of a file to use as the value.
  * `decodeHTML`: If `true`, the value will be unescaped.
  * `parseHTML`: If `true`, the html value will be converted to simple markdown, compatible with Message Cards.

#### Example

``` yaml
params:
  template: |
    {
      "@type": "MessageCard",
      "@context": "https://schema.org/extensions",
      "summary": "{title}",
      "themeColor": "35495c",
      "title": "{title}",
      "text": "{text}",
      "potentialAction": [{
        "@type": "OpenUri",
        "name": "View",
        "targets": [{
          "os": "default",
          "uri": "{link}"
        }]
      }]
    }
  vars:
    title:
      file: path/to/title-file
    text:
      file: path/to/content-file
      parseHTML: true
      decodeHTML: true
    link:
      file: path/to/link-file
```



