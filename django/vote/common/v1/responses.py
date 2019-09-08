from rest_framework.response import Response


class MetaDataResponse(Response):
    meta_data_dict = {
        "meta": "",
        "data": {}
    }

    def __init__(self, *args, **kwargs):
        if args:
            MetaDataResponse.meta_data_dict["data"] = args[0]
            if len(args) >= 2:
                MetaDataResponse.meta_data_dict["meta"] = args[1]
            modified_args = tuple([MetaDataResponse.meta_data_dict])
        super(MetaDataResponse, self).__init__(*modified_args, **kwargs)
