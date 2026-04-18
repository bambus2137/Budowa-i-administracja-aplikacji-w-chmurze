import { useEffect, useState } from "react";
import axios from "axios";

const API = import.meta.env.VITE_API_URL + "/tasks/";

type Task = {
  id: number;
  title: string;
  completed: boolean;
};

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState("");
  const [editingId, setEditingId] = useState<number | null>(null);
  const [editText, setEditText] = useState("");

  const fetchTasks = async () => {
    const res = await axios.get<Task[]>(API);
    setTasks(res.data);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const createTask = async () => {
    if (!title.trim()) return;
    const res = await axios.post<Task>(API, { title });
    setTasks([res.data, ...tasks]);
    setTitle("");
  };

  const deleteTask = async (id: number) => {
    await axios.delete(`${API}${id}/`);
    setTasks(tasks.filter((t) => t.id !== id));
  };

  const toggleComplete = async (task: Task) => {
    const updated = { ...task, completed: !task.completed };
    await axios.put(`${API}${task.id}/`, updated);
    setTasks(tasks.map((t) => (t.id === task.id ? updated : t)));
  };

  const startEdit = (task: Task) => {
    setEditingId(task.id);
    setEditText(task.title);
  };

  const saveEdit = async (task: Task) => {
    const updated = { ...task, title: editText };
    await axios.put(`${API}${task.id}/`, updated);
    setTasks(tasks.map((t) => (t.id === task.id ? updated : t)));
    setEditingId(null);
  };

  return (
    <div className="container">
      <h1>Cloud Task Manager</h1>

      <div className="input-row">
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Add a task..."
        />
        <button onClick={createTask}>Add</button>
      </div>

      <ul className="taskbar">
        {tasks.map((task) => (
          <li key={task.id} className="task">
            {editingId === task.id ? (
              <>
                <input
                  value={editText}
                  onChange={(e) => setEditText(e.target.value)}
                />
                <button onClick={() => saveEdit(task)}>Save</button>
              </>
            ) : (
              <>
                <span
                  onClick={() => toggleComplete(task)}
                  className={task.completed ? "done" : ""}
                >
                  {task.title}
                </span>

                <div className="actions">
                  <button onClick={() => startEdit(task)}>Update</button>
                  <button onClick={() => deleteTask(task.id)}>Delete</button>
                </div>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
