<div class="pusher"><div class="undefined disable-select"><div class="problems_header_content__o_4YA"><div class="problems_header_content__title__L2cB2 g-mb-0"><h3 class="g-m-0">Peak element</h3></div><i id="bug_1" aria-hidden="true" class="bug icon"></i></div><div class="problems_header_description__t_8PB"><span>Accuracy: <strong>46.67%</strong></span><span>Submissions: <strong>15+</strong></span><span>Points: <strong>3</strong></span></div><div class="ui divider"></div><div><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an array <strong>arr[]&nbsp;</strong>where no two adjacent elements are same, find the <strong>index </strong>of a <strong>peak </strong>element. An element is considered to be a <strong>peak</strong> if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them.&nbsp;</span><span style="font-size: 18.6667px;">The output will be&nbsp;</span><strong style="font-size: 18.6667px;">"true"</strong><span style="font-size: 18.6667px;">&nbsp;if the index returned by your function is correct; otherwise, it will be "</span><strong style="font-size: 18.6667px;">false"</strong><span style="font-size: 18.6667px;">.</span></p>
<p><span style="font-size: 14pt;">Note: Consider the element <strong>before </strong>the <strong>first </strong>element and the element <strong>after </strong>the <strong>last </strong>element to be <strong>negative infinity</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples :<br></strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [1, 2, 4, 5, 7, 8, 3]
<strong>Output:</strong> true
<strong>Explanation: </strong>arr[5] = 8 is a peak element because arr[4] &lt; arr[5] &gt; arr[6].</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [10, 20, 15, 2, 23, 90, 80]
<strong>Output: </strong>true<strong>
Explanation: </strong>arr[1] = 20 and arr[5] = 90 are peak elements because arr[0] &lt; arr[1] &gt; arr[2] and arr[4] &lt; arr[5] &gt; arr[6]. <br></span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr = [1, 2, 3]
<strong>Output: </strong>true<strong>
Explanation: </strong>arr[2] is a peak element because arr[1] &lt; arr[2] and arr[2] is the last element, so it has negative infinity to its right.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br><span style="font-size: 18.6667px;">1</span>&nbsp;≤ arr.size() ≤ 10<sup>6</sup><br>-2<sup>31</sup> ≤ arr[i] ≤ 2<sup>31</sup> - 1</span></p></div></div>
