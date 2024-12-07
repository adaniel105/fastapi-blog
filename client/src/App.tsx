import { ModeToggle } from "@/components/mode-toggle"


export default function App(){
  return(
    <div className="mt-20 ml-20 max-w-3xl">
      <div className="fixed top-2 right-2">
        <ModeToggle  />
      </div>
      <h1 className="text-4xl">All Blogs</h1>
      <ul className="my-6 ml-6 list-disc [&>li]:mt-2">
        <li>Blog 1</li>
        <li>Blog 2</li>
        <li>Blog 3</li>
        <li>Blog 4</li>
        <li>Blog 5</li>
      </ul>

    </div>
  )
}