import express, { Request, Response } from "express";
// import { getData } from "./src/services/database";
// import databaseRoute from "./src/routes/database-route";
const app = express();
const PORT = 3007;

app.use(express.json());

app.get('/api/', (req: Request, res: Response) => {
    res.send('API of my app');
});

// app.use('/api/data', getData);

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
