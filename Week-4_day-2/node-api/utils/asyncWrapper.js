const asyncWrapper = (fn) => {
    return async(req, res) => {
        try{
            await fn(req, res);
        }catch(err){
            req.error=err;
            throw err;

        }
    };
};

module.exports = asyncWrapper;