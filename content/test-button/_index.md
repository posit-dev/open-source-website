---
title: "Test: Button Shortcode"
layout: single
---

## Basic button

```
{{</* button url="https://posit.co" text="Visit Posit" */>}}
```

{{< button url="https://posit.co" text="Visit Posit" >}}

## Button with icon and text

```
{{</* button url="https://github.com/posit-dev" icon="simple-icons--github" text="GitHub" */>}}
```

{{< button url="https://github.com/posit-dev" icon="simple-icons--github" text="GitHub" >}}

## Icon-only button

```
{{</* button url="https://github.com/posit-dev" icon="simple-icons--github" alt="Posit on GitHub" */>}}
```

{{< button url="https://github.com/posit-dev" icon="simple-icons--github" alt="Posit on GitHub" >}}

## Button with target="_blank"

```
{{</* button url="https://posit.co" text="Open in new tab" target="_blank" icon="boxicons--link-external" */>}}
```

{{< button url="https://posit.co" text="Open in new tab" target="_blank" icon="boxicons--link-external" >}}

## Button with custom class

```
{{</* button url="https://posit.co" text="Custom styled" class="bg-green-500 hover:bg-green-600 rounded-full" */>}}
```

{{< button url="https://posit.co" text="Custom styled" class="bg-green-500 hover:bg-green-600 rounded-full" >}}

## Button with icon and custom text

```
{{</* button url="https://posit.co" icon="boxicons--download" text="Download now" */>}}
```

{{< button url="https://posit.co" icon="boxicons--download" text="Download now" >}}

## Multiple buttons

{{< button url="https://posit.co" text="Primary" >}}
{{< button url="https://posit.co" text="Secondary" class="bg-gray-500 hover:bg-gray-600" >}}
{{< button url="https://posit.co" icon="simple-icons--github" text="GitHub" class="bg-gray-800 hover:bg-gray-900" >}}
