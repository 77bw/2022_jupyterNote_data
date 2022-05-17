function gettime(){
    $.ajax({
        url:"/time",
        timeout:10000,
        success:function(data){
            $("#time").html(data)
        },
        error:function(xhr,type,errorThrown){

        }
      

    });
    }
 function get_c1_data(){
    $.ajax({
            url:"/c1",/*数据发送给c1路由*/
            success:function(data){
            $(".num h1").eq(0).text(data.confirm);
            $(".num h1").eq(1).text(data.suspect);
            $(".num h1").eq(2).text(data.heal);
            $(".num h1").eq(3).text(data.dead);
        },
        error:function(xhr,type,errorThrown){
        }
        })
    }

function get_c2_data() {
	$.ajax({
		url:"/c2",
		success: function(data) {
			optionMap.series[0].data = data.data
			ec_center.setOption(optionMap)
		},
		error: function(xhr, type, errorThrown) {
		}
	})
}
#获取左1，ajax的数据请求
function get_l1_data() {
	$.ajax({
		url:"/l1",
		success: function(data) {
		    option_left1.xAxis.data=data.day
		    option_left1.series[0].data=data.confirm
            option_left1.series[1].data=data.suspect
            option_left1.series[2].data=data.heal
            option_left1.series[3].data=data.dead
            ec_left1.setOption(option_left1)
		},
		error: function(xhr, type, errorThrown) {
		}
	})
}

#获取左2，ajax的数据请求
function get_l2_data() {
	$.ajax({
		url:"/l2",
		success: function(data) {
		    option_left2.xAxis.data=data.day
		    option_left2.series[0].data=data.confirm_add
            option_left2.series[1].data=data.suspect_add
            ec_left2.setOption(option_left2)
		},
		error: function(xhr, type, errorThrown) {
		}
	})
}
setInterval(gettime,1000)  //每隔1s调用gettime函数

get_c1_data()
get_c2_data()
get_l1_data()
get_l2_data()