var app = angular.module('LoganLogin',[]);
app.controller('LoganCtl', function($scope){
    $scope.test="fanish";
    $scope.reinitMsgs = function(){
        $scope.message = "";
        $scope.message_type = "";
        }

    $scope.setSuccessMessage = function(msg, type){
        $scope.setMessage(msg, 'success');
    }
    $scope.setErrorMessage = function(msg, type){
        $scope.setMessage(msg, 'danger');
    }
    $scope.log_me = function(){
        $scope.bindLogin($scope);
    }
    $scope.setMessage = function(msg, type){
        console.log("Message" + type + " : " + msg);
        $scope.message = msg;
        $scope.message_type = type;
    }
    $scope.bindLogin = function($scope){

        $scope.reinitMsgs();
        res = logan.bind_login($scope.username, $scope.password);
        if (res == ""){
            $scope.setSuccessMessage("CONNECTION_SUCCESS");
        } else {
            $scope.setErrorMessage(res);
        }
    }
});



