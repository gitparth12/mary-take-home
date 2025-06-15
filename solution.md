## Dev Log

### Initial Plan

Given 400 something pages, simplify approach to one entry per page

1. For each page, look for full text or vector search keywords
2. Choose one of the found ones (or skip current page if none found)
3. Use one of the templates to insert text based on the keyword found
4. Might have to look into some traditional NLP to accomplish this

### Second Plan

After doing some research, it became clear that plain manipulation of text with
traditional NLP would not be possible in the given time frame, possibly because
of my lack of experience in this area.

Through the handful of research papers I glossed over, using an LLM for
synthetic dataset generation seemed like a surprisingly common method and
having worked with LLMs before, I believe this will work better than the last
strategy could.

I plan to implement both local and api-based models, probably one each. The
most crucial part of this approach is probably handling the prompt, and
ensuring accurate data. The first one is pretty straightforward, I just have to
be careful with how I structure the prompt. For the second, I want to give the
LLM the option to not generate data if it didn't find it (assuming I give small
chunks of the corpora), and also ask it to validate the accuracy of what it
generated post-hoc. The second one might be out of scope if I run out of time.

I decided to make two classes, one for running Gemini through its API and
another to run inference locally. Before I implement local inference, I'd like
to run through Gemini to validate feasibility and then extend using local
inference. The next step in the process is probably to write the actual prompt,
then split the ocr text by pages so that I can generate in batches to retain
context properly, and finally bring everything together into a pipeline and
generate data. Some helper functions may be required along the way, and I'll
try to keep everything fairly extensible.

I tested an arbitrary prompt with gemini and generation is working as expected.
I also decided to use ai to help me write some regex that would parse a
response output into a json object. The output is expected to be a list of
objects, each following the dataset row format provided. Next, I'm planning to
implement a simple function that splits the ocr document by the page numbers.
Finally, I'll write a function that reads the ocr document, splits it, and then
iteratively provides each page to gemini. It will then take all of that output
and write it to a .jsonl file. Since we already have the pages, I plan to add
the page number to each row of the dataset. Might help with SFT.

I encountered resource limits while working with the Gemini API and was able to
limit the input to only 10 pages to get around it for now. I expect this to not
cause any issues later but will consume some credits to confirm when
everything's done. For now, I'll move onto local inference.

Through a quick google search, I decided to use Mistral 7B v0.3 model to make
another class similar to the one with Gemini. Since I'll be using huggingface
for this, it should be easy to just replace the model name string to change the
model used.
