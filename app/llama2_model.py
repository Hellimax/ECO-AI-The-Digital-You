import replicate




def generate_personlised_tweet(tweet_raw_text,topic_discription):


    initial_promt = "Following are some sample tweets, based on the sample tweets given below, generate a tweet in the style of the sample tweets (in the writing style of the sample tweets) in the given topic in 60 words \n\n sample tweets: \n\n"

    ending_prompt = "topic:"+topic_discription

    final_prompt = initial_promt+tweet_raw_text+ending_prompt

    #print(final_prompt)

    output = replicate.run(
        "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
        input={
            "prompt": final_prompt
        }
    )
    final_output = "".join(list(output))

    return final_output
    # for item in output:
    #     print(item, end="")

if __name__=="__main__":
    generate_personlised_tweet()