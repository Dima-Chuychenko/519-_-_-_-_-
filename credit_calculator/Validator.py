class Validator:

    def __init__(self, args_, *args, **kwargs):
        self.args_ = args_
        self._validate()

    def _validate(self):

        params = {}

        if not self.args_.__dict__.get("type"):
            raise AttributeError("flag type is requiered")
        if self.args_.__dict__.get("type") not in ("annuity", "diff"):
            raise AttributeError("flag type must consist with annuity or diff param")

        if self.args_.__dict__.get("principal"):
            if not int(self.args_.__dict__.get("principal")) > 0:
                raise AttributeError("flag principal is or incorrect")
            params["principal"] = self.args_.__dict__.get("principal")

        if self.args_.__dict__.get("payments"):
            print(self.args_.__dict__.get("payments"))
            if int(self.args_.__dict__.get("payments")) > int(self.args_.__dict__.get("principal")) or not \
                    int(self.args_.__dict__.get("payments")) > 0:
                raise AttributeError("flag payment is incorrect")
            params["payments"] = self.args_.__dict__.get("payments")

        if self.args_.__dict__.get("interest"):
            if not 100 > int(self.args_.__dict__.get("interest")) > 0:
                raise AttributeError("flag interest is incorrect")
            params["interest"] = self.args_.__dict__.get("interest")

        if self.args_.__dict__.get("periods"):
            if not int(self.args_.__dict__.get("periods")) > 0:
                raise AttributeError("flag periods is incorrect")
            params["periods"] = self.args_.__dict__.get("periods")
        params["type"] = self.args_.__dict__.get("type")
        if len(params) != 4:
            return params
        return False
