def greeter():
    name = yield "What is your name?"  # yield OUT, wait for send()
    yield f"Hello, {name}!"            # use value sent IN

g = greeter()
print(next(g))        # Starts generator, runs until first yield → "What is your name?"
print(g.send("Raj"))  # Sends "Raj" into the generator, resumes from the yield line
