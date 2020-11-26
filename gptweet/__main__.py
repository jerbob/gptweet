import io, os, sys
from contextlib import redirect_stdout

import gpt_2_simple as gpt2

from gptweet import make_tweet


sys.stderr = io.StringIO()
stdout_buffer = io.StringIO()

session = gpt2.start_tf_sess()
gpt2.load_gpt2(session, run_name="run1")

with redirect_stdout(stdout_buffer):
    gpt2.generate(
        session,
        run_name="run1",
        temperature=0.7,
        nsamples=1,
        batch_size=1,
        truncate="\n",
    )

tweet = stdout_buffer.getvalue().replace("<Image>", "").strip()
with open("tweet.png", "wb") as file:
    file.write(make_tweet(tweet))
