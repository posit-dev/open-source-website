---
title: "Starting to think about AI Fairness"
description: |
  The topic of AI fairness metrics is as important to society as it is confusing. Confusing it is due to a number of reasons: terminological proliferation, abundance of formulae, and last not least the impression that everyone else seems to know what they're talking about. This text hopes to counteract some of that confusion by starting from a common-sense approach of contrasting two basic positions: On the one hand, the assumption that dataset features may be taken as reflecting the underlying concepts ML practitioners are interested in; on the other, that there inevitably is a gap between concept and measurement, a gap that may be bigger or smaller depending on what is being measured. In contrasting these fundamental views, we bring together concepts from ML, legal science, and political philosophy.
date: 2021-07-15
categories:
  - R
  - Concepts
  - Meta
  - AI & Society
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
image: thumbnail.jpg
ported_from: ai
port_status: in-progress
---



If you use deep learning for unsupervised part-of-speech tagging of
Sanskrit [^1], or knowledge discovery in physics [^2], you probably
don't need to worry about model fairness. If you're a data scientist
working at a place where decisions are made about *people*, however, or
an academic researching models that will be used to such ends, chances
are that you've already been thinking about this topic. --- Or feeling that
you should. And thinking about this is hard.

It is hard for several reasons. In this text, I will go into *just one*.

## The forest for the trees

Nowadays, it is hard to find a modeling framework that does *not*
include functionality to assess fairness. (Or is at least planning to.)
And the terminology sounds so familiar, as well: "calibration",
"predictive parity", "equal true \[false\] positive rate"... It almost
seems as though we could just take the metrics we make use of anyway
(recall or precision, say), test for equality across groups, and that's
it. Let's assume, for a second, it really was that simple. Then the
question still is: Which metrics, exactly, do we choose?

In reality things are *not* simple. And it gets worse. For very good
reasons, there is a close connection in the ML fairness literature to
concepts that are primarily treated in other disciplines, such as the
legal sciences: *discrimination* and *disparate impact* (both not being
far from yet another statistical concept, *statistical parity*).
Statistical parity means that if we have a classifier, say to decide
whom to hire, it should result in as many applicants from the
disadvantaged group (e.g., Black people) being hired as from the
advantaged one(s). But that is quite a different requirement from, say,
equal true/false positive rates!

So despite all that abundance of software, guides, and decision trees,
even: This is not a simple, technical decision. It is, in fact, a
technical decision only to a small degree.

## Common sense, not math

Let me start this section with a disclaimer: Most of the sources
referenced in this text appear, or are implied on the ["Guidance"
page](http://aif360.mybluemix.net/resources#guidance) of IBM's framework
AI Fairness 360. If you read that page, and everything that's said and
not said there appears clear from the outset, then you may not need this
more verbose exposition. If not, I invite you to read on.

Papers on fairness in machine learning, as is common in fields like
computer science, abound with formulae. Even the papers referenced here,
though selected not for their theorems and proofs but for the ideas they
harbor, are no exception. But to start thinking about fairness as it
might apply to an ML process at hand, common language -- and common
sense -- will do just fine. If, after analyzing your use case, you judge
that the more technical results *are* relevant to the process in
question, you will find that their verbal characterizations will often
suffice. It is only when you doubt their correctness that you will need
to work through the proofs.

At this point, you may be wondering what it is I am contrasting those
"more technical results" with. This is the topic of the next section,
where I'll try to give a birds-eye characterization of fairness criteria
and what they imply.

## Situating fairness criteria

Think back to the example of a hiring algorithm. What does it mean for
this algorithm to be fair? We approach this question under two --
incompatible, mostly -- assumptions:

1.  The algorithm is fair if it behaves the same way independent of
    which demographic group it is applied to. Here demographic group
    could be defined by ethnicity, gender, abledness, or in fact any
    categorization suggested by the context.

2.  The algorithm is fair if it does not discriminate against any
    demographic group.

I'll call these the technical and societal views, respectively.

### Fairness, viewed the technical way

What does it mean for an algorithm to "behave the same way" regardless
of which group it is applied to?

In a classification setting, we can view the relationship between
prediction ($\hat{Y}$) and target ($Y$) as a doubly directed path. In
one direction: Given true target $Y$, how accurate is prediction
$\hat{Y}$? In the other: Given $\hat{Y}$, how well does it predict the
true class $Y$?

Based on the direction they operate in, metrics popular in machine
learning overall can be split into two categories. In the first,
starting from the true target, we have *recall*, together with "the
*rate*s": true positive, true negative, false positive, false negative.
In the second, we have *precision*, together with positive (negative,
resp.) *predictive value*.

If now we demand that these metrics be the same across groups, we arrive
at corresponding fairness criteria: equal false positive rate, equal
positive predictive value, etc. In the inter-group setting, the two
types of metrics may be arranged under headings "equality of
opportunity" and "predictive parity". You'll encounter these as actual
headers in the summary table at the end of this text.

<aside>

Said table organizes concepts from different areas into a three-category
format. The overall narrative builds up towards that "map" in a
bottom-up way -- meaning, most entries will not make sense at this
point.

</aside>

While overall, the terminology around metrics can be confusing (to me it
is), these headings have some mnemonic value. *Equality of opportunity*
suggests that people similar in real life ($Y$) get classified similarly
($\hat{Y}$). *Predictive parity* suggests that people classified
similarly ($\hat{Y}$) are, in fact, similar ($Y$).

The two criteria can concisely be characterized using the language of
statistical independence. Following Barocas et al. (2019), these are:

- Separation: Given true target $Y$, prediction $\hat{Y}$ is
  independent of group membership ($\hat{Y} \perp A | Y$).

- Sufficiency: Given prediction $\hat{Y}$, target $Y$ is independent
  of group membership ($Y \perp A | \hat{Y}$).

Given those two fairness criteria -- and two sets of corresponding
metrics -- the natural question arises: Can we satisfy both? Above, I
was mentioning precision and recall on purpose: to maybe "prime" you to
think in the direction of "precision-recall trade-off". And really,
these two categories reflect different preferences; usually, it is
impossible to optimize for both. The most famous, probably, result is
due to Chouldechova (2016) : It says that predictive parity (testing
for sufficiency) is incompatible with error rate balance (separation)
when prevalence differs across groups. This is a theorem (yes, we're in
the realm of theorems and proofs here) that may not be surprising, in
light of Bayes' theorem, but is of great practical importance
nonetheless: Unequal prevalence usually is the norm, not the exception.

This necessarily means we have to make a choice. And this is where the
theorems and proofs *do* matter. For example, Yeom and Tschantz (2018) show that
in this framework -- the strictly technical approach to fairness --
separation should be preferred over sufficiency, because the latter
allows for arbitrary disparity amplification. Thus, *in this framework*,
we may have to work through the theorems.

What is the alternative?

### Fairness, viewed as a social construct

Starting with what I just wrote: No one will likely challenge fairness
*being* a social construct. But what does that entail?

Let me start with a biographical reminiscence. In undergraduate
psychology (a long time ago), probably the most hammered-in distinction
relevant to experiment planning was that between a hypothesis and its
operationalization. The hypothesis is what you want to substantiate,
conceptually; the operationalization is what you measure. There
necessarily can't be a one-to-one correspondence; we're just striving to
implement the best operationalization possible.

In the world of datasets and algorithms, all we have are measurements.
And often, these are treated *as though* they were the concepts. This
will get more concrete with an example, and we'll stay with the hiring
software scenario.

Assume the dataset used for training, assembled from scoring previous
employees, contains a set of predictors (among which, high-school
grades) and a target variable, say an indicator whether an employee did
"survive" probation. There is a concept-measurement mismatch on both
sides.

For one, say the grades are intended to reflect ability to learn, and
motivation to learn. But depending on the circumstances, there
are influence factors of much higher impact: socioeconomic status,
constantly having to struggle with prejudice, overt discrimination, and
more.

And then, *the target variable*. If the thing it's supposed to measure
is "was hired for seemed like a good fit, and was retained since was a
good fit", then all is good. But normally, HR departments are aiming for
more than just a strategy of "keep doing what we've always been doing".

Unfortunately, that concept-measurement mismatch is even more fatal,
and even less talked about, when it's about the target and not the
predictors. (Not accidentally, we also call the target the "ground
truth".) An infamous example is recidivism prediction, where what we
really want to measure -- whether someone did, in fact, commit a crime
-- is replaced, for measurability reasons, by whether they were
convicted. These are not the same: Conviction depends on more
then what someone has done -- for instance, if they've been under
intense scrutiny from the outset.

Fortunately, though, the mismatch is clearly pronounced in the AI
fairness literature. Friedler et al. (2016) distinguish between the *construct*
and *observed* spaces; depending on whether a near-perfect mapping is
assumed between these, they talk about two "worldviews": "We're all
equal" (WAE) vs. "What you see is what you get" (WYSIWIG). If we're all
equal, membership in a societally disadvantaged group should not -- in
fact, may not -- affect classification. In the hiring scenario, any
algorithm employed thus has to result in the same proportion of
applicants being hired, regardless of which demographic group they
belong to. If "What you see is what you get", we don't question that the
"ground truth" *is* the truth.

This talk of worldviews may seem unnecessary philosophical, but the
authors go on and clarify: All that matters, in the end, is whether the
data is seen as reflecting reality in a naïve, take-at-face-value way.

For example, we might be ready to concede that there could be small,
albeit uninteresting effect-size-wise, statistical differences between
men and women as to spatial vs. linguistic abilities, respectively. We
know for sure, though, that there are much greater effects of
socialization, starting in the core family and reinforced,
progressively, as adolescents go through the education system. We
therefore apply WAE, trying to (partly) compensate for historical
injustice. This way, we're effectively applying affirmative action,
[defined as](https://www.law.cornell.edu/wex/affirmative_action)

> A set of procedures designed to eliminate unlawful discrimination
> among applicants, remedy the results of such prior discrimination, and
> prevent such discrimination in the future.

In the already-mentioned summary table, you'll find the WYSIWIG
principle mapped to both equal opportunity and predictive parity
metrics. WAE maps to the third category, one we haven't dwelled upon
yet: *demographic parity*, also known as *statistical parity*. In line
with what was said before, the requirement here is for each group to be
present in the positive-outcome class in proportion to its
representation in the input sample. For example, if thirty percent of
applicants are Black, then at least thirty percent of people selected
should be Black, as well. A term commonly used for cases where this does
*not* happen is *disparate impact*: The algorithm affects different
groups in different ways.

Similar in spirit to demographic parity, but possibly leading to
different outcomes in practice, is conditional demographic parity [^3].
Here we additionally take into account other predictors in the dataset;
to be precise: *all* other predictors. The desiderate now is that for
any choice of attributes, outcome proportions should be equal, given the
protected attribute **and** the other attributes in question. I'll come
back to why this may sound better in theory than work in practice in the
next section.

Summing up, we've seen commonly used fairness metrics organized into
three groups, two of which share a common assumption: that the data used
for training can be taken at face value. The other starts from the
outside, contemplating what historical events, and what political and
societal factors have made the given data look as they do.

Before we conclude, I'd like to try a quick glance at other disciplines,
beyond machine learning and computer science, domains where fairness
figures among the central topics. This section is necessarily limited in
every respect; it should be seen as a flashlight, an invitation to read
and reflect rather than an orderly exposition. The short section will
end with a word of caution: Since drawing analogies can feel highly
enlightening (and is intellectually satisfying, for sure), it is easy to
abstract away practical realities. But I'm getting ahead of myself.

## A quick glance at neighboring fields: law and political philosophy

In jurisprudence, fairness and discrimination constitute an important
subject. A recent paper that caught my attention is Wachter et al. (2020a) . From a
machine learning perspective, the interesting point is the
classification of metrics into bias-preserving and bias-transforming.
The terms speak for themselves: Metrics in the first group reflect
biases in the dataset used for training; ones in the second do not. In
that way, the distinction parallels Friedler et al. (2016) 's confrontation of
two "worldviews". But the exact words used also hint at how guidance by
metrics feeds back into society: Seen as strategies, one preserves
existing biases; the other, to consequences unknown a priori, *changes
the world*.

To the ML practitioner, this framing is of great help in evaluating what
criteria to apply in a project. Helpful, too, is the systematic mapping
provided of metrics to the two groups; it is here that, as alluded to
above, we encounter *conditional demographic parity* among the
bias-transforming ones. I agree that in spirit, this metric can be seen
as bias-transforming; if we take two sets of people who, per all
available criteria, are equally qualified for a job, and then find the
whites favored over the Blacks, fairness is clearly violated. But the
problem here is "available": per all *available* criteria. What if we
have reason to assume that, in a dataset, all predictors are biased?
Then it will be very hard to prove that discrimination has occurred.

A similar problem, I think, surfaces when we look at the field of
political philosophy, and consult theories on [distributive
justice](https://plato.stanford.edu/entries/justice-distributive/) for
guidance. Heidari et al. (2018) have written a paper comparing the three
criteria -- demographic parity, equality of opportunity, and predictive
parity -- to egalitarianism, equality of opportunity (EOP) in the
Rawlsian sense, and EOP seen through the glass of luck egalitarianism,
respectively. While the analogy is fascinating, it too assumes that we
may take what is in the data at face value. In their likening predictive
parity to luck egalitarianism, they have to go to especially great
lengths, in assuming that the *predicted* class reflects *effort
exerted*. In the below table, I therefore take the liberty to disagree,
and map a libertarian view of distributive justice to both equality of
opportunity and predictive parity metrics.

In summary, we end up with two highly controversial categories of
fairness criteria, one bias-preserving, "what you see is what you
get"-assuming, and libertarian, the other bias-transforming, "we're all
equal"-thinking, and egalitarian. Here, then, is that often-announced
table.

<table style="width:94%;">
<colgroup>
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th></th>
<th>Demographic
parity</th>
<th>Equality of
opportunity</th>
<th>Predictive
parity</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>A.K.A. /
subsumes /
related
concepts</strong></td>
<td>statistical
parity, group
fairness,
disparate
impact,
conditional
demographic
parity <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>equalized
odds, equal
false positive
/ negative
rates</td>
<td>equal positive
/ negative
predictive
values,
calibration by
group</td>
</tr>
<tr>
<td><strong>Statistical
independence
criterion</strong>
<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
<td><p>independence</p>
<p><span class="math inline"><em>Ŷ</em> ⟂ <em>A</em></span></p></td>
<td><p>separation</p>
<p><span class="math inline"><em>Ŷ</em> ⟂ <em>A</em>|<em>Y</em></span></p></td>
<td><p>sufficiency</p>
<p><span class="math inline"><em>Y</em> ⟂ <em>A</em>|<em>Ŷ</em></span></p></td>
</tr>
<tr>
<td><strong>Individual /
group</strong></td>
<td>group</td>
<td>group (most)
or individual
(fairness
through
awareness)</td>
<td>group</td>
</tr>
<tr>
<td><strong>Distributive
Justice</strong></td>
<td>egalitarian</td>
<td>libertarian
(contra
Heidari et
al., see
above)</td>
<td>libertarian
(contra
Heidari et
al., see
above)</td>
</tr>
<tr>
<td><strong>Effect on
bias</strong> <a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a></td>
<td>transforming</td>
<td>preserving</td>
<td>preserving</td>
</tr>
<tr>
<td><strong>Policy /
“worldview”</strong>
<a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a></td>
<td>We’re all
equal (WAE)</td>
<td>What you see
is what you
get (WYSIWIG)</td>
<td>What you see
is what you
get (WYSIWIG)</td>
</tr>
</tbody>
</table>
<section id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p><span class="citation" data-cites="abs-2005-05906">Wachter et al. (2020b)</span><a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p><span class="citation" data-cites="barocas">Barocas et al. (2019)</span><a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p><span class="citation" data-cites="nondisc">Wachter et al. (2020a)</span><a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4"><p><span class="citation" data-cites="FriedlerSV16">Friedler et al. (2016)</span><a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</section>

## (A) Conclusion

In line with its original goal -- to provide some help in starting to
think about AI fairness metrics -- this article does not end with
recommendations. It does, however, end with an observation. As the last
section has shown, amidst all theorems and theories, all proofs and
memes, it makes sense to not lose sight of the concrete: the data trained
on, and the ML process as a whole. Fairness is not something to be
evaluated post hoc; the *feasibility of fairness* is to be reflected on
right from the beginning.

In that regard, assessing impact on fairness is not that different from
that essential, but often toilsome and non-beloved, stage of modeling
that precedes the modeling itself: exploratory data analysis.

Thanks for reading!

Photo by <a href="https://unsplash.com/@andersjilden?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Anders Jildén</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Barocas, Solon, Moritz Hardt, and Arvind Narayanan. 2019. *Fairness and Machine Learning*. Fairmlbook.org.

Chouldechova, Alexandra. 2016. "<span class="nocase">Fair prediction with disparate impact: A study of bias in recidivism prediction instruments</span>." *arXiv e-Prints*, October, arXiv:1610.07524. <https://arxiv.org/abs/1610.07524>.

Cranmer, Miles D., Alvaro Sanchez-Gonzalez, Peter W. Battaglia, et al. 2020. "Discovering Symbolic Models from Deep Learning with Inductive Biases." *CoRR* abs/2006.11287. <https://arxiv.org/abs/2006.11287>.

Friedler, Sorelle A., Carlos Scheidegger, and Suresh Venkatasubramanian. 2016. "On the (Im)possibility of Fairness." *CoRR* abs/1609.07236. <http://arxiv.org/abs/1609.07236>.

Heidari, Hoda, Michele Loi, Krishna P. Gummadi, and Andreas Krause. 2018. "A Moral Framework for Understanding of Fair ML Through Economic Models of Equality of Opportunity." *CoRR* abs/1809.03400. <http://arxiv.org/abs/1809.03400>.

Srivastava, Prakhar, Kushal Chauhan, Deepanshu Aggarwal, Anupam Shukla, Joydip Dhar, and Vrashabh Prasad Jain. 2018. "Deep Learning Based Unsupervised POS Tagging for Sanskrit." *Proceedings of the 2018 International Conference on Algorithms, Computing and Artificial Intelligence* (New York, NY, USA), ACAI 2018. <https://doi.org/10.1145/3302425.3302487>.

Wachter, Sandra, Brent D. Mittelstadt, and Chris Russell. 2020a. "Bias Preservation in Machine Learning: The Legality of Fairness Metrics Under EU Non-Discrimination Law." *West Virginia Law Review, Forthcoming* abs/2005.05906. <https://ssrn.com/abstract=3792772>.

Wachter, Sandra, Brent D. Mittelstadt, and Chris Russell. 2020b. "Why Fairness Cannot Be Automated: Bridging the Gap Between EU Non-Discrimination Law and AI." *CoRR* abs/2005.05906. <https://arxiv.org/abs/2005.05906>.

Yeom, Samuel, and Michael Carl Tschantz. 2018. "Discriminative but Not Discriminatory: A Comparison of Fairness Definitions Under Different Worldviews." *CoRR* abs/1808.08619. <http://arxiv.org/abs/1808.08619>.

[^1]: Srivastava et al. (2018)

[^2]: Cranmer et al. (2020)

[^3]: Wachter et al. (2020b)
