var log = function() {
  console.log(arguments)
}

var todoTemplate = function(todo){
  var t = todo
  s = `
  <div class="todo-cell" data-id="${ t.id }">
    <span class="todo-task">${ t.task }</span>
    <a href="#" class="todo-delete">删除</a>
    <a href="#" class="todo-edit">编辑</a>
    <div class="todo-edit-cell hide">
      <input class="todo-update-input">
      <button class="todo-update-button">更新</button>
    </div>
  </div>
  `
  return s
}

//绑定添加微博事件
var bindEventTodoAdd = function(){
  $('#id-todo-button').on('click', function(){
    var task = $('#id-todo-input').val()
    var form = {
      task: task,
    }
    var request = {
      url: '/api/todo/add',
      type: 'post',
      data: form,
      success: function(response){
        log('成功', arguments)
        var t = JSON.parse(response)
        $('.todo-container').append(todoTemplate(t))
      },
      error: function(){
        log('失败', arguments)
      },
    }
    $.ajax(request)
  })
}

//绑定删除微博事件
var bindEventTodoDelete = function(){
  $('.todo-container').on('click', '.todo-delete', function(){
    var todoCell = $(this).closest('.todo-cell')
    var todoId = $(todoCell).data('id')
    log('debug todoId', todoId)
    var request = {
      url: '/api/todo/delete/' + todoId,
      type: 'post',
      success: function(response){
        log('成功', arguments)
        $(todoCell).slideUp()
      },
      error: function(){
        log('失败', arguments)
      },
    }
    $.ajax(request)
  })
}

//展开更新栏事件
var bindEventTodoEdit = function(){
  $('.todo-container').on('click', '.todo-edit', function(){
    var todoEditCell = $(this).closest('.todo-cell').find('.todo-edit-cell')
    $(todoEditCell).toggle()
  })
}

//绑定更新微博事件
var bindEventTodoUpdate = function(){
  $('.todo-container').on('click', '.todo-update-button', function(){
    var todoCell = $(this).closest('.todo-cell')
    var todoId = $(todoCell).data('id')
    var task = $(todoCell).find('.todo-update-input').val()
    var form = {
      task: task,
    }
    var request = {
      url: '/api/todo/update/' + todoId,
      type: 'post',
      data: form,
      success: function(response){
        log('成功', arguments)
        $(todoCell).find('.todo-task').text(task)
      },
      error: function(){
        log('失败', arguments)
      },
    }
    $.ajax(request)
  })
}

$(document).ready(function(){
  bindEventTodoAdd()
  bindEventTodoDelete()
  bindEventTodoEdit()
  bindEventTodoUpdate()
})
