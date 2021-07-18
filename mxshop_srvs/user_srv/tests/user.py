import time

import grpc

from user_srv.proto import user_pb2_grpc, user_pb2


class UserTest:
    def __init__(self):
        channel = grpc.insecure_channel("127.0.0.1:8091")
        self.stub = user_pb2_grpc.UserStub(channel)

    def user_list(self):
        rsp: user_pb2.UserListResponse = self.stub.GetUserList(user_pb2.PageInfo(pSize=2))
        print(rsp.total)
        for user in rsp.data:
            print(user.mobile, user.birthday)

    def get_user_by_id(self, id):
        rsp: user_pb2.UserInfoResponse = self.stub.GetUserById(user_pb2.IdRequest(id=id))
        print(rsp.mobile)

    def get_user_by_mobile(self, mobile):
        user: user_pb2.UserInfoResponse = self.stub.GetUserByMobile(user_pb2.MobileRequest(mobile=mobile))
        print(user)

    def create_user(self, nick_name, mobile, password):
        user: user_pb2.UserInfoResponse = self.stub.CreateUser(user_pb2.CreateUserInfo(
            nickName=nick_name,
            mobile=mobile,
            password=password
        ))
        print(user)

    def update_user(self, id, gender, nick_name, birthday):
        user = self.stub.UpdateUser(user_pb2.UpdateUserInfo(id=id, gender=gender, nickName=nick_name, birthday=birthday))
        print(user)

if __name__ == "__main__":
    user = UserTest()
    user.user_list()
    # user.get_user_by_id(2)
    # user.get_user_by_mobile("18782222221")
    # user.create_user(nick_name='boby1', mobile='1823491371', password='123456')
    # user.update_user(id=1, gender='female', nick_name='xj', birthday=int(round(time.time())))