---
title: "Test: Video Shortcode"
layout: single
---

## YouTube (short URL)

```
{{</* video src="https://youtu.be/wo9vZccmqwc" */>}}
```

{{< video src="https://youtu.be/wo9vZccmqwc" >}}

## YouTube (watch URL)

```
{{</* video src="https://www.youtube.com/watch?v=wo9vZccmqwc" */>}}
```

{{< video src="https://www.youtube.com/watch?v=wo9vZccmqwc" >}}

## YouTube (embed URL)

```
{{</* video src="https://www.youtube.com/embed/wo9vZccmqwc" */>}}
```

{{< video src="https://www.youtube.com/embed/wo9vZccmqwc" >}}

## YouTube with start time and title

```
{{</* video src="https://youtu.be/wo9vZccmqwc" start="116" title="What is the CERN?" */>}}
```

{{< video src="https://youtu.be/wo9vZccmqwc" start="116" title="What is the CERN?" >}}

## YouTube with fixed size

```
{{</* video src="https://youtu.be/wo9vZccmqwc" width="400" height="300" */>}}
```

{{< video src="https://youtu.be/wo9vZccmqwc" width="400" height="300" >}}

## YouTube with 21:9 aspect ratio

```
{{</* video src="https://youtu.be/wo9vZccmqwc" aspect-ratio="21x9" */>}}
```

{{< video src="https://youtu.be/wo9vZccmqwc" aspect-ratio="21x9" >}}

## YouTube with 4:3 aspect ratio

```
{{</* video src="https://youtu.be/wo9vZccmqwc" aspect-ratio="4x3" */>}}
```

{{< video src="https://youtu.be/wo9vZccmqwc" aspect-ratio="4x3" >}}

## Vimeo

```
{{</* video src="https://vimeo.com/548291297" */>}}
```

{{< video src="https://vimeo.com/548291297" >}}

## Local video file

```
{{</* video src="local-video.mp4" title="Demo video" */>}}
```
