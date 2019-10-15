/*
 * --------------------------------------- 
 * Copyright (c) 2019 enrique.chen@live.cn
 * --------------------------------------- 
 */
#ifndef INCLUDE_PIORUN_WORKER_H_
#define INCLUDE_PIORUN_WORKER_H_

#include <string>
#include <exception>

namespace Piorun {
enum WorkerStatus {
    W_UNKOWN, W_BUSY, W_AVAILABLE, W_LOADED, W_CRUSHED, W_STOPPED
};

enum TaskStatus {
        T_UNKOWN, T_DUPLICATED, T_SUCCEED, T_FAILED, T_TIMEOUT
    };
struct ProcessResult {
    std::exception e;
    TaskStatus status;
    std::string cst_msg;
};

class WInterface {
 public:
    virtual ~WInterface() = 0;
    virtual std::string OrderType() = 0;
    virtual std::exception Config(const std::string &runtime_conf) = 0;
    virtual int Process(ProcessResult* const result) = 0;
    virtual std::exception Terminate() = 0;
};

struct Payload {
    std::string catena;
    std::string trace_id;
    std::string runtime_conf;
    std::string task;
    std::exception e;
};

class PInterface {
 public:
    virtual ~PInterface() = 0;
    virtual std::string OrderType() = 0;
    virtual int Publish(Payload* const payload) = 0;
};

}  // namespace Piorun

#endif  // INCLUDE_PIORUN_WORKER_H_
