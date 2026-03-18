---
title: "Test: Button Shortcode"
layout: single
---

## Basic button (external URL auto-gets external icon and target="_blank")

```
{{</* button url="https://posit.co" text="Visit Posit" */>}}
```

{{< button url="https://posit.co" text="Visit Posit" >}}

## Button with icon-left and text

```
{{</* button url="https://github.com/posit-dev" icon="simple-icons--github" text="GitHub" */>}}
```

{{< button url="https://github.com/posit-dev" icon="simple-icons--github" text="GitHub" >}}

## Icon-only button

```
{{</* button url="https://github.com/posit-dev" icon="simple-icons--github" alt="Posit on GitHub" */>}}
```

{{< button url="https://github.com/posit-dev" icon="simple-icons--github" alt="Posit on GitHub" >}}

## Button with icon-right

```
{{</* button url="/events/" text="See all events" icon-right="boxicons--arrow-right" */>}}
```

{{< button url="/events/" text="See all events" icon-right="boxicons--arrow-right" >}}

## Button with both icon-left and icon-right

```
{{</* button url="https://github.com/posit-dev" icon-left="simple-icons--github" icon-right="boxicons--arrow-right" text="GitHub" */>}}
```

{{< button url="https://github.com/posit-dev" icon-left="simple-icons--github" icon-right="boxicons--arrow-right" text="GitHub" >}}

## External button with suppressed external icon

```
{{</* button url="https://posit.co" text="No external icon" icon-right="false" */>}}
```

{{< button url="https://posit.co" text="No external icon" icon-right="false" >}}

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
{{< button url="https://posit.co" icon="simple-icons--linkedin" text="LinkedIn" class="bg-gray-800 hover:bg-gray-900" >}}
