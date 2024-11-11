// import {Router, Request, Response} from "express";

// import {getData} from '../services/database'

// const router = Router();

// router.get('/', async (req: Request, res: Response) => {
//     const name = req.query.name as string;
//     if (name) {
//         const pokemon = await getData(name);
//         res.json(pokemon);
//         return;
//     } else {
//         const pokemon = await getData();
//         res.json(pokemon);
//     }
// });

// export default router;