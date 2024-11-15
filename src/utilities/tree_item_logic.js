export default {
  
  findTreeItem(items, id) {
    var self = this; 
    if (!items) {
      return;
    }
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      // Test current object
      if (item.FolderId === id) {
        return item;
      }
      // Test children recursively
      const child = self.findTreeItem(item.Children, id);
      if (child) {
        return child;
      }
    }
  },
  getTreeItemsList(items) {
    if (!items) {
        // Do nothing
        return;
    }
    for (var i = 0; i < items.length; i++) {
        var item = items[i];
        // Test current object
          //console.log("Name: " + item.Name + " Folder: " + item.FolderId)
          this.imageFolderIdList.push(item.FolderId)
        // Test children recursively
        const child = this.getTreeItemsList(item.Children);
    }
    return (Math.max(...this.imageFolderIdList))
  },
  async delFolder(itemSelected, objFrom) {
    if(itemSelected.Children[0])
    {
      //Confirm if you want to delete all items in the folder. 
      //insert if condition
      //Recurssively delete all children items first. 
      var items = itemSelected.Children
      for (var i = 0; i < items.length; i++) {
        var item = items[i];
        this.delActiveTreeObject(item)
      }
    }
    //Delete actual folder
    this.delObject(itemSelected, objFrom)
  },
  async delObject(itemSelected, objFrom) {
    console.log("Deleted: " + itemSelected.Name + " FolderId: " + itemSelected.FolderId)
    objFrom.splice(objFrom.indexOf(itemSelected), 1);
    
  },
}