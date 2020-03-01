from pulumi.dynamic import Resource, ResourceProvider, CreateResult, UpdateResult
from pulumi import Input, Output
from .tag_provider import TagProvider


class TagArgs(object):
    workspace_path: Input[str]
    tag_name: Input[str]
    tracking_id: Input[str]

    def __init__(self, workspace_path, tag_name, tracking_id):
        self.workspace_path = workspace_path
        self.tag_name = tag_name
        self.tracking_id = tracking_id


class Tag(Resource):
    tag_id: Output[str]
    path: Output[str]

    def __init__(self, name, args: TagArgs, opts=None):
        full_args = {tag_id: None, path: None, **vars(args)}
        super().__init__(TagProvider(), name, full_args, opts)
