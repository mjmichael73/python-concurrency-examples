Note: A thread pool is a pattern for achieving concurrency of execution in a program. A thread pool allows us to automatically manage a pool of threads efficiently.

Note: Each thread in the pool is called a worker.

Note: You can reuse the thread after the work is done.

Note: It protects against failures such as exceptions.

Note: You can create Thread Pool using ThreadPoolExecutor. 

Note: The ThreadPoolExecutor has 3 methods to control the thread pool:

    - submit()  -> Dispatch a function to be executed and return a Future object. The submit function takes a function and executes it asynchrounously.
    - map() -> Executes a function asynchrounously for each element in an iterable.
    - shutdown() -> Shut down the executor.


### Future object:

A Future is an object that represents the eventual result of an asynchronous operation. The future class has two useful methods:

    - result() -> Returns the result of asynchrounous operation.
    - exception() -> Returns the execption of an asynchrounous operation in case of an exception.
