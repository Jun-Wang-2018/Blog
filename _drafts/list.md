---
layout: post
---
1.  Sample first item.

    This is a result statement that talks about something....

2.  Continuing the list

    <div markdown="span" class="alert alert-info" role="alert"><i class="fa fa-info-circle"></i> <b>Note:</b> Remember to do this. If you have "quotes", you must escape them.</div>


    Here's a list in here:

    * first item
    * second item

3.  Another list item.

    ```js
    function alert("hello");
    ```

4.  Another item.
    1. sub-list numbered one
    2. sub-list numbered two
    {% katexmm %}
      This is a mixed environment where you can have normal text and $c = \pm\sqrt{a^2 + b^2}$ fenced math.
    {% endkatexmm %}

    {% katex display %}
      c = \pm\sqrt{a^2 + b^2}
      \mathcal O
      \nabla_\boldsymbol{x} J(\boldsymbol{x})
    {% endkatex %}

    {% katexmm %}
      $ c = \pm\sqrt{a^2 + b^2} $

      $ \mathcal O $

      $ \nabla_\boldsymbol{x} J(\boldsymbol{x}) $
    {% endkatexmm %}

    $$ \mathcal O $$


    $$ \nabla_\boldsymbol{x} J(\boldsymbol{x}) $$
